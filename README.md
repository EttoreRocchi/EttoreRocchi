<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <img src="assets/banner-light.svg" width="100%" alt="Ettore Rocchi - Health Researcher at IRCCS Sant'Orsola. Physics background, biomedical mission.">
</picture>

<p align="center">
  <a href="https://ettorerocchi.github.io"><img src="https://img.shields.io/badge/Website-EttoreRocchi.github.io-2E7D32?style=flat&logo=githubpages&logoColor=white" alt="Website"></a>
  <a href="https://www.linkedin.com/in/ettore-rocchi/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://bsky.app/profile/ettorerocchi.bsky.social"><img src="https://img.shields.io/badge/Bluesky-0285FF?style=flat&logo=bluesky&logoColor=white" alt="Bluesky"></a>
  <a href="mailto:ettore.rocchi@aosp.bo.it"><img src="https://img.shields.io/badge/Email-ettore.rocchi%40aosp.bo.it-grey?style=flat&logo=gmail&logoColor=white" alt="Email"></a>
  <br>
  <a href="https://scholar.google.com/citations?user=MKHoGnQAAAAJ"><img src="https://img.shields.io/badge/Google_Scholar-4285F4?style=flat&logo=Google-Scholar&logoColor=white" alt="Google Scholar"></a>
  <a href="https://orcid.org/0000-0002-7612-2819"><img src="https://img.shields.io/badge/ORCID-0000--0002--7612--2819-A6CE39?style=flat&logo=orcid&logoColor=white" alt="ORCID"></a>
  <a href="https://www.scopus.com/authid/detail.uri?authorId=57220152522"><img src="https://img.shields.io/badge/Scopus-E9711C?style=flat&logo=Scopus&logoColor=white" alt="Scopus"></a>
</p>

I'm a Health Researcher at IRCCS Sant'Orsola in Bologna, where I develop computational methods to predict antimicrobial resistance, discover patient phenotypes, and make sense of high-dimensional omics data. My work spans MALDI-TOF mass spectrometry, multi-omics integration, genomics, and metagenomics, always with a focus on interpretability and clinical impact. I work in the Computational Genomics Unit, part of the Multi-Omics and Health-Care Data Analytics Unit at Sant'Orsola Hospital, and collaborate closely with Prof. Gastone Castellani's [Physics4MedicineLab](https://github.com/Physics4MedicineLab).

PhD in Health and Technologies (University of Bologna, 2026), supervisor Prof. Gastone Castellani.

---

### [MaldiSuite Ecosystem](https://github.com/EttoreRocchi/MaldiSuite)

<div align="center">
  <a href="https://github.com/EttoreRocchi/MaldiSuite">
    <img src="https://raw.githubusercontent.com/EttoreRocchi/MaldiSuite/main/assets/maldi_suite_logo.png" width="420" alt="MaldiSuite" />
  </a>
</div>

> **[MaldiSuite](https://github.com/EttoreRocchi/MaldiSuite)** - a Python ecosystem for MALDI-TOF spectral processing and analysis in antimicrobial resistance research. Visit the [MaldiSuite website](https://ettorerocchi.github.io/MaldiSuite/).

Three sklearn-compatible packages that chain into an end-to-end clinical AMR pipeline: preprocess with **MaldiAMRKit**, harmonise across batches/sites with **MaldiBatchKit**, classify with **MaldiDeepKit**.

```bash
pip install maldisuite   # MaldiAMRKit + MaldiBatchKit + MaldiDeepKit
```

<div align="center">
  <a href="https://github.com/EttoreRocchi/MaldiAMRKit">
    <img src="https://raw.githubusercontent.com/EttoreRocchi/MaldiSuite/main/assets/maldiamrkit_logo.png" height="140" alt="MaldiAMRKit" />
  </a>
  <a href="https://github.com/EttoreRocchi/MaldiBatchKit">
    <img src="https://raw.githubusercontent.com/EttoreRocchi/MaldiSuite/main/assets/maldibatchkit_logo.png" height="140" alt="MaldiBatchKit" />
  </a>
  <a href="https://github.com/EttoreRocchi/MaldiDeepKit">
    <img src="https://raw.githubusercontent.com/EttoreRocchi/MaldiSuite/main/assets/maldideepkit_logo.png" height="140" alt="MaldiDeepKit" />
  </a>
</div>

<p align="center">
  <a href="https://pypi.org/project/maldiamrkit/"><img src="https://static.pepy.tech/personalized-badge/maldiamrkit?period=total&units=international_system&left_color=grey&right_color=blue&left_text=MaldiAMRKit" alt="MaldiAMRKit downloads"></a>
  <a href="https://pypi.org/project/maldibatchkit/"><img src="https://static.pepy.tech/personalized-badge/maldibatchkit?period=total&units=international_system&left_color=grey&right_color=blue&left_text=MaldiBatchKit" alt="MaldiBatchKit downloads"></a>
  <a href="https://pypi.org/project/maldideepkit/"><img src="https://static.pepy.tech/personalized-badge/maldideepkit?period=total&units=international_system&left_color=grey&right_color=blue&left_text=MaldiDeepKit" alt="MaldiDeepKit downloads"></a>
</p>

---

### Python Packages

| Package | Description | PyPI | Downloads |
|---------|-------------|------|-----------|
| [combatlearn](https://github.com/EttoreRocchi/combatlearn) | Scikit-learn compatible ComBat batch-effect correction | [![PyPI](https://img.shields.io/pypi/v/combatlearn?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/combatlearn/) | ![combatlearn downloads](https://static.pepy.tech/personalized-badge/combatlearn?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads) |
| [ResPredAI](https://github.com/EttoreRocchi/ResPredAI) | AI model to predict resistances in Gram-negative bloodstream infections | [![PyPI](https://img.shields.io/pypi/v/respredai?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/respredai/) | ![ResPredAI downloads](https://static.pepy.tech/personalized-badge/respredai?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads) |
| [phenocluster](https://github.com/EttoreRocchi/phenocluster) | Unsupervised clinical phenotype discovery with survival and multistate modeling | [![PyPI](https://img.shields.io/pypi/v/phenocluster?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/phenocluster/) | ![phenocluster downloads](https://static.pepy.tech/personalized-badge/phenocluster?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads) |
| [nestkit](https://github.com/EttoreRocchi/nestkit) | Nested cross-validation with calibration, threshold optimization, and statistical tests | [![PyPI](https://img.shields.io/pypi/v/nestkit?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/nestkit/) | ![nestkit downloads](https://static.pepy.tech/personalized-badge/nestkit?period=total&units=international_system&left_color=grey&right_color=blue&left_text=downloads) |

### Research Code

| Project | Description |
|---------|-------------|
| [CATS](https://github.com/Physics4MedicineLab/CATS) | Automated Cas9 nuclease comparison with ClinVar integration |
| [CAMISIM-BrokenStick](https://github.com/Physics4MedicineLab/CAMISIM-BrokenStick) | Broken stick model extension for metagenomic simulation |
| [APOBECSeeker](https://github.com/Physics4MedicineLab/APOBECSeeker) | APOBEC-style mutation identification from multiple sequence alignment |

---

### Research Focus

- **AMR & clinical machine learning** - MALDI-TOF, supervised & generative learning, cross-site harmonisation · [MaldiSuite](https://github.com/EttoreRocchi/MaldiSuite), [ResPredAI](https://github.com/EttoreRocchi/ResPredAI)
- **Infectious risk & pathogen surveillance** - patient phenotyping, survival & multi-state models, metagenomic surveillance · [phenocluster](https://github.com/EttoreRocchi/phenocluster), [CAMISIM-BrokenStick](https://github.com/Physics4MedicineLab/CAMISIM-BrokenStick)
- **Computational genomics** - structural variants, somatic calling, long-read sequencing · [APOBECSeeker](https://github.com/Physics4MedicineLab/APOBECSeeker), [CATS](https://github.com/Physics4MedicineLab/CATS)
- **Computational methodologies** - open-source tools, reproducible pipelines · [combatlearn](https://github.com/EttoreRocchi/combatlearn), [nestkit](https://github.com/EttoreRocchi/nestkit), [MaldiBatchKit](https://github.com/EttoreRocchi/MaldiBatchKit)

The full picture is on the [research page](https://ettorerocchi.github.io/research.html) of my website.

### Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat&logo=gnubash&logoColor=white)
![Snakemake](https://img.shields.io/badge/Snakemake-3B8526?style=flat&logo=snakemake&logoColor=white)
![Nextflow](https://img.shields.io/badge/Nextflow-0DC09D?style=flat&logo=nextflow&logoColor=white)

---

### Selected Publication

Bonazzetti, C., Rocchi, E. *et al.* [Artificial Intelligence model to predict resistances in Gram-negative bloodstream infections](https://doi.org/10.1038/s41746-025-01696-x). *npj Digital Medicine* **8**, 319 (2025). Code: [ResPredAI](https://github.com/EttoreRocchi/ResPredAI).

A curated list with BibTeX lives on [my website](https://ettorerocchi.github.io/publications.html); for the complete record, see my [Google Scholar](https://scholar.google.com/citations?user=MKHoGnQAAAAJ) profile.
