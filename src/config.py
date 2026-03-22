TRAIN_PATH = "data/training_dataset.csv"
TEST_PATH = "data/testing_dataset.csv"

STATE_MODEL_PATH = "models/state_model.pkl"
INTENSITY_MODEL_PATH = "models/intensity_model.pkl"

TEXT_COL = "journal_text"

NUM_COLS = [
    "sleep_hours",
    "energy_level",
    "stress_level",
    "duration_min"
]

CAT_COLS = [
    "time_of_day",
    "ambience_type"
]

TARGET_STATE = "emotional_state"
TARGET_INTENSITY = "intensity"