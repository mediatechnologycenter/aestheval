# aestheval

This repo allows make easy to access and process different datasets used usually for aesthetic assessment methods, as well as the newly introduced Reddit Photo Critique Dataset.

## Get Reddit PhotoCritique Dataset
__Zenodo:__ [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6656802.svg)](https://doi.org/10.5281/zenodo.6656802)


__HF datasets:__ Coming soon...

Files in the dataset:

- ``reddit_photocritique_posts.pkl`` - 260.7 MB - Processed posts of Reddit
- ``raw_reddit_photocritique_comments.csv`` - 279.0 MB - File with allt he comments belonging to every post. Not processed.
- ``processed_info_test.json`` - 208.6 MB - Test set as used for trainings and analysis	
- ``processed_info_train.json`` - 725.7 MB 	- Train set as used for trainings and analysis
- ``processed_info_validation.json`` - 104.7 MB - Validation set as used for trainings and analysis



## Steps

### 1. Create environment

```
conda env create -f environment.yml
pip install -e .
```

### 2. Download datasets

Follow the README in the directory `data/` to download at least the images from Reddit.

### 3. Process Reddit dataset

```
python aestheval/data/reddit/prepare_dataset.py --only_predictions  # Reads the provided dataframe.
```

Use the `--reddit_dir` argument to set the directory where you downloaded ``reddit_photocritique_posts.pkl`` file. Default is `data/`. If posts and comments were not downloaded before, not setting --only_predictions argument will make the script to throw erros.

### 4. Predict sentiment of comments and compute informativeness score

On PCCD, AVA and Reddit (takes a while)

```
python main.py --compute_sentiment_score --compute_informativeness_score
```

Already processed files can be found under `data/`. This directory can be changed using the `--data_path` argument. This step produces the files you downloaded from Zenodo:
- ``processed_info_test.json`` 
- ``processed_info_train.json`` 
- ``processed_info_validation.json``

## Repo structure (WIP)

The repo is structured as follows:
- `EDAs`: Exploratory Data Analysis of AVA, DPC, PCCD and RPCD, as well as the concatenation of them all.
- `aestheval`: Library with the data utils to download, load and process data; as well with the baselines used in this project.
- `results`: Results of the expeeriments with Aesthetic ViT, ViT + Linear probe and NIMA.


## Cite
If you use this dataset, please cite the following paper:
* Nieto, Daniel Vera, Luigi Celona, and Clara Fernandez-Labrador. "Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment." arXiv preprint arXiv:2206.08614 (2022) [[PDF]](https://arxiv.org/abs/2206.08614).

```
@misc{nieto2022understanding,
    title={Understanding Aesthetics with Language: A Photo Critique Dataset for Aesthetic Assessment},
    author={Daniel Vera Nieto and Luigi Celona and Clara Fernandez-Labrador},
    year={2022},
    eprint={2206.08614},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
