# Human Detection Using AI Model

This project aims to identify people and activities from radar recordings for drone detection.

## Project goal

Given one radar recording, the model should estimate:

- Whether a person is present
- The activity: crawling, walking, or running
- The person's distance from the radar, when distance ground-truth labels are available

## Dataset

The current working dataset is organized into activity folders. Each recording is provided as a `.bin` file with a matching capture log `.txt` and raw log `.csv`.

Current inventory: 34 recordings — 22 walking, 8 running, 3 crawling, and 1 `no_detection`. The `no_detection` recording is confirmed to mean no person is present. The `.bin` files are the radar signal input; capture logs describe the sensor configuration.

## Current status

- Dataset files have been inventoried and companion files checked.
- Folder names provide provisional activity labels.
- Distance labels still need verification against the original experiment notes. Do not treat a distance mentioned in a folder name as ground truth until confirmed.
- The radar binary format and sensor configuration must be decoded consistently before training.
- The dataset is small and imbalanced, especially for the no-human class, so more labeled recordings will be needed for reliable evaluation.

## Planned workflow

1. Verify activity, human-presence, and distance labels for each recording.
2. Decode `.bin` files using the capture configuration and convert them into consistent radar samples/features.
3. Split data by complete recording (and collection session where possible) into training, validation, and test sets to avoid data leakage.
4. Train activity/presence classification and distance estimation; evaluate each output separately on recordings not used for training.
5. Test the complete prediction workflow with new recordings and report uncertainty for unsupported or unfamiliar cases.
