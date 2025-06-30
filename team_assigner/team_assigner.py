from sklearn.cluster import KMeans
import numpy as np

class TeamAssigner:
    def __init__(self):
        self.team_colors = {}
        self.player_team_dict = {}
    
    def get_clustering_model(self,image):
        # Check if image is empty or has invalid dimensions
        if image.size == 0 or image.shape[0] == 0 or image.shape[1] == 0:
            raise ValueError("Input image is empty or has invalid dimensions")
            
        # Reshape the image to 2D array
        image_2d = image.reshape(-1,3)
        
        # Check if reshaped array has valid dimensions
        if image_2d.shape[0] == 0:
            raise ValueError("Reshaped image array has 0 samples")

        # Preform K-means with 2 clusters
        kmeans = KMeans(n_clusters=2, init="k-means++",n_init=1)
        kmeans.fit(image_2d)

        return kmeans

    def get_player_color(self,frame,bbox):
        # Validate bounding box coordinates
        x1, y1, x2, y2 = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        
        # Ensure coordinates are within frame bounds
        height, width = frame.shape[:2]
        x1 = max(0, min(x1, width))
        y1 = max(0, min(y1, height))
        x2 = max(0, min(x2, width))
        y2 = max(0, min(y2, height))
        
        # Check if bounding box has valid dimensions
        if x2 <= x1 or y2 <= y1:
            # Return a default color if bounding box is invalid
            return np.array([128, 128, 128])  # Gray color as default
        
        image = frame[y1:y2, x1:x2]
        
        # Check if image is empty
        if image.size == 0:
            return np.array([128, 128, 128])  # Gray color as default
        
        # Check if image has valid dimensions for top half
        if image.shape[0] < 2:
            return np.array([128, 128, 128])  # Gray color as default
            
        top_half_image = image[0:int(image.shape[0]/2),:]

        # Get Clustering model
        kmeans = self.get_clustering_model(top_half_image)

        # Get the cluster labels forr each pixel
        labels = kmeans.labels_

        # Reshape the labels to the image shape
        clustered_image = labels.reshape(top_half_image.shape[0],top_half_image.shape[1])

        # Get the player cluster
        corner_clusters = [clustered_image[0,0],clustered_image[0,-1],clustered_image[-1,0],clustered_image[-1,-1]]
        non_player_cluster = max(set(corner_clusters),key=corner_clusters.count)
        player_cluster = 1 - non_player_cluster

        player_color = kmeans.cluster_centers_[player_cluster]

        return player_color


    def assign_team_color(self,frame, player_detections):
        
        player_colors = []
        for _, player_detection in player_detections.items():
            bbox = player_detection["bbox"]
            try:
                player_color = self.get_player_color(frame,bbox)
                player_colors.append(player_color)
            except Exception as e:
                print(f"Warning: Failed to get player color for bbox {bbox}: {e}")
                # Skip this detection if it fails
                continue
        
        # Check if we have enough valid player colors
        if len(player_colors) < 2:
            print("Warning: Not enough valid player colors for clustering. Using default team colors.")
            self.team_colors[1] = np.array([255, 0, 0])  # Red
            self.team_colors[2] = np.array([0, 0, 255])  # Blue
            return
        
        kmeans = KMeans(n_clusters=2, init="k-means++",n_init=10)
        kmeans.fit(player_colors)

        self.kmeans = kmeans

        self.team_colors[1] = kmeans.cluster_centers_[0]
        self.team_colors[2] = kmeans.cluster_centers_[1]


    def get_player_team(self,frame,player_bbox,player_id):
        if player_id in self.player_team_dict:
            return self.player_team_dict[player_id]

        try:
            player_color = self.get_player_color(frame,player_bbox)
        except Exception as e:
            print(f"Warning: Failed to get player color for player {player_id}: {e}")
            # Assign to team 1 as default
            self.player_team_dict[player_id] = 1
            return 1

        team_id = self.kmeans.predict(player_color.reshape(1,-1))[0]
        team_id+=1

        if player_id ==91:
            team_id=1

        self.player_team_dict[player_id] = team_id

        return team_id
