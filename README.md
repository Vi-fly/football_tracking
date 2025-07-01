# Soccer Video Analysis System

A comprehensive computer vision system for analyzing soccer videos with advanced tracking, team identification, ball possession analysis, and performance metrics.

## 🚀 Features

### 1. **Multi-Object Tracking**
- **YOLO-based Detection**: Uses YOLO model for detecting players, referees, and the ball
- **ByteTrack Tracking**: Implements ByteTrack algorithm for robust object tracking across frames
- **Ball Position Interpolation**: Automatically fills missing ball positions using interpolation
- **Position Tracking**: Tracks both center positions and foot positions for different objects

### 2. **Team Assignment System**
- **Color-based Clustering**: Uses K-means clustering to identify team colors from player jerseys
- **Automatic Team Detection**: Automatically assigns players to teams based on jersey colors
- **Visual Team Indicators**: Displays players with team-specific colors (red/blue)

### 3. **Ball Possession Analysis**
- **Player-Ball Assignment**: Determines which player has possession of the ball
- **Distance-based Logic**: Uses proximity analysis to assign ball possession
- **Team Ball Control Statistics**: Tracks and displays ball possession percentages for each team
- **Real-time Updates**: Shows ball control statistics throughout the video

### 4. **Camera Movement Compensation**
- **Optical Flow Analysis**: Detects camera movement using Lucas-Kanade optical flow
- **Feature Point Tracking**: Tracks stable feature points to estimate camera motion
- **Position Adjustment**: Compensates for camera movement in object tracking
- **Movement Visualization**: Displays camera movement metrics on screen

### 5. **View Transformation**
- **Perspective Transformation**: Converts camera view to top-down field view
- **Field Calibration**: Maps pixel coordinates to real-world field dimensions
- **Coordinate System**: Transforms positions to standard soccer field coordinates (68m x 23.32m)

### 6. **Speed and Distance Estimation**
- **Player Speed Calculation**: Calculates player speed in km/h
- **Distance Tracking**: Tracks total distance covered by each player
- **Frame-based Analysis**: Uses sliding window approach for smooth speed calculations
- **Real-time Display**: Shows speed and distance metrics above each player

### 7. **Advanced Visualization**
- **Player Annotations**: Displays player IDs with colored ellipses
- **Ball Tracking**: Shows ball position with triangle markers
- **Team Color Coding**: Different colors for different teams
- **Statistics Overlay**: Real-time display of ball possession and camera movement
- **Performance Metrics**: Speed and distance information for each player

## 🛠️ Technical Architecture

### Core Components

1. **Tracker** (`trackers/tracker.py`)
   - YOLO model integration
   - ByteTrack implementation
   - Ball position interpolation
   - Visualization functions

2. **Team Assigner** (`team_assigner/team_assigner.py`)
   - K-means clustering for color analysis
   - Team color detection
   - Player team assignment

3. **Player-Ball Assigner** (`player_ball_assigner/player_ball_assigner.py`)
   - Proximity-based ball assignment
   - Distance calculation logic

4. **Camera Movement Estimator** (`camera_movement_estimator/camera_movement_estimator.py`)
   - Optical flow analysis
   - Camera motion compensation
   - Movement visualization

5. **View Transformer** (`view_transformer/view_transformer.py`)
   - Perspective transformation
   - Field coordinate mapping

6. **Speed and Distance Estimator** (`speed_and_distance_estimator/speed_and_distance_estimator.py`)
   - Speed calculation
   - Distance tracking
   - Performance metrics display

## ✅ Running on Kaggle

1. **Open the notebook** on Kaggle.

2. **Attach datasets** containing:
   - The detection model (`best.pt`)
   - The input video

3. **Run all cells in sequence.**

4. The output video will be saved in:
```bash
/kaggle/working/output_videos/output_video.mp4
```
## 💻 Local Run
## 📋 Requirements

```bash
ultralytics
supervision
opencv-python
numpy
matplotlib
pandas
scikit-learn
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd soccer-video-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLO model**
   - Place your trained YOLO model in the `models/` directory
   - Update the model path in `main.py` if needed

## 📹 Usage

### Basic Usage

1. **Prepare your video**
   - Place your soccer video in the `input_videos/` directory
   - Update the video path in `main.py`

2. **Run the analysis**
   ```bash
   python main.py
   ```

3. **View results**
   - Processed video will be saved in `output_videos/` directory
   - The output includes all annotations and metrics

### Configuration

- **Model Path**: Update `model_path` in `main.py` to use your YOLO model
- **Video Path**: Change the input video path in the `read_video()` function
- **Stub Files**: Use existing stub files for faster processing (set `read_from_stub=True`)

## 📊 Output Features

The processed video includes:

- **Player Tracking**: Colored ellipses with player IDs
- **Team Identification**: Different colors for each team
- **Ball Possession**: Visual indicators for ball possession
- **Speed Metrics**: Real-time speed display for each player
- **Distance Tracking**: Total distance covered by players
- **Ball Control Statistics**: Team possession percentages
- **Camera Movement**: Movement metrics display

## 🔧 Customization

### Field Calibration
Update the `pixel_vertices` in `view_transformer.py` to match your field dimensions:

```python
self.pixel_vertices = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
```

### Team Colors
Modify the clustering parameters in `team_assigner.py` for different team color schemes.

### Speed Calculation
Adjust the `frame_window` parameter in `speed_and_distance_estimator.py` for different speed calculation intervals.

## 📁 Project Structure

```
├── main.py                          # Main execution script
├── requirements.txt                 # Python dependencies
├── models/                          # YOLO model directory
├── input_videos/                    # Input video files
├── output_videos/                   # Processed output videos
├── stubs/                          # Cached processing data
├── trackers/                       # Object tracking module
├── team_assigner/                  # Team identification module
├── player_ball_assigner/           # Ball possession analysis
├── camera_movement_estimator/      # Camera motion compensation
├── view_transformer/               # Perspective transformation
├── speed_and_distance_estimator/   # Performance metrics
└── utils/                          # Utility functions
```

## 🎯 Use Cases

- **Sports Analytics**: Player performance analysis
- **Coaching Tools**: Tactical analysis and player evaluation
- **Broadcasting**: Enhanced sports coverage with real-time statistics
- **Research**: Computer vision and sports analytics research

## 🔍 Technical Details

### Detection Classes
- **Player**: Soccer players (including goalkeepers)
- **Referee**: Match officials
- **Ball**: Soccer ball

### Coordinate Systems
- **Pixel Coordinates**: Original video frame coordinates
- **Adjusted Coordinates**: Camera movement compensated coordinates
- **Field Coordinates**: Real-world field dimensions (meters)

### Performance Metrics
- **Speed**: Calculated in km/h using distance/time
- **Distance**: Total distance covered in meters
- **Ball Possession**: Percentage of time each team controls the ball

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- YOLO for object detection
- ByteTrack for multi-object tracking
- OpenCV for computer vision operations
- Supervision for detection utilities

---

**Note**: This system is designed for soccer video analysis and may require calibration for different field types or camera setups.
