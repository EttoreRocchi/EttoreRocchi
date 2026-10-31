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

<p align="center">
  <a href="https://ettorerocchi.github.io/research.html">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&size=20&duration=3500&pause=1200&color=E3A86A&center=true&vCenter=true&width=640&height=40&lines=From+mass+spectra+to+resistance+predictions;From+patient+trajectories+to+pathogen+spread;From+raw+reads+to+clinically+usable+variants;From+clinical+needs+to+open-source+frameworks">
      <img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&size=20&duration=3500&pause=1200&color=9E5622&center=true&vCenter=true&width=640&height=40&lines=From+mass+spectra+to+resistance+predictions;From+patient+trajectories+to+pathogen+spread;From+raw+reads+to+clinically+usable+variants;From+clinical+needs+to+open-source+frameworks" alt="From mass spectra to resistance predictions, from patient trajectories to pathogen spread, from raw reads to clinically usable variants, from clinical needs to open-source frameworks">
    </picture>
  </a>
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

<table align="center">
  <tr>
    <th><div align="center">Preprocess</div></th>
    <th><div align="center">Harmonise</div></th>
    <th><div align="center">Classify</div></th>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/EttoreRocchi/MaldiAMRKit"><img src="assets/logo-maldiamrkit.png" height="160" alt="MaldiAMRKit" /></a></td>
    <td align="center"><a href="https://github.com/EttoreRocchi/MaldiBatchKit"><img src="assets/logo-maldibatchkit.png" height="160" alt="MaldiBatchKit" /></a></td>
    <td align="center"><a href="https://github.com/EttoreRocchi/MaldiDeepKit"><img src="assets/logo-maldideepkit.png" height="160" alt="MaldiDeepKit" /></a></td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://maldiamrkit.readthedocs.io/"><img src="https://img.shields.io/readthedocs/maldiamrkit?style=flat&logo=readthedocs&logoColor=white" alt="MaldiAMRKit docs"></a><br>
      <a href="https://github.com/EttoreRocchi/MaldiAMRKit/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/EttoreRocchi/MaldiAMRKit/ci.yml?branch=main&style=flat&logo=githubactions&logoColor=white&label=CI" alt="MaldiAMRKit CI"></a><br>
      <a href="https://codecov.io/github/EttoreRocchi/MaldiAMRKit"><img src="https://img.shields.io/codecov/c/github/EttoreRocchi/MaldiAMRKit?style=flat&logo=codecov&logoColor=white" alt="MaldiAMRKit coverage"></a>
    </td>
    <td align="center">
      <a href="https://maldibatchkit.readthedocs.io/"><img src="https://img.shields.io/readthedocs/maldibatchkit?style=flat&logo=readthedocs&logoColor=white" alt="MaldiBatchKit docs"></a><br>
      <a href="https://github.com/EttoreRocchi/MaldiBatchKit/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/EttoreRocchi/MaldiBatchKit/ci.yml?branch=main&style=flat&logo=githubactions&logoColor=white&label=CI" alt="MaldiBatchKit CI"></a><br>
      <a href="https://codecov.io/github/EttoreRocchi/MaldiBatchKit"><img src="https://img.shields.io/codecov/c/github/EttoreRocchi/MaldiBatchKit?style=flat&logo=codecov&logoColor=white" alt="MaldiBatchKit coverage"></a>
    </td>
    <td align="center">
      <a href="https://maldideepkit.readthedocs.io/"><img src="https://img.shields.io/readthedocs/maldideepkit?style=flat&logo=readthedocs&logoColor=white" alt="MaldiDeepKit docs"></a><br>
      <a href="https://github.com/EttoreRocchi/MaldiDeepKit/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/EttoreRocchi/MaldiDeepKit/ci.yml?branch=main&style=flat&logo=githubactions&logoColor=white&label=CI" alt="MaldiDeepKit CI"></a><br>
      <a href="https://codecov.io/github/EttoreRocchi/MaldiDeepKit"><img src="https://img.shields.io/codecov/c/github/EttoreRocchi/MaldiDeepKit?style=flat&logo=codecov&logoColor=white" alt="MaldiDeepKit coverage"></a>
    </td>
  </tr>
</table>

---

### Python Packages

| Package | Description | PyPI |
|---------|-------------|------|
| [combatlearn](https://github.com/EttoreRocchi/combatlearn) | Scikit-learn compatible ComBat batch-effect correction | [![PyPI](https://img.shields.io/pypi/v/combatlearn?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/combatlearn/) |
| [ResPredAI](https://github.com/EttoreRocchi/ResPredAI) | AI model to predict resistances in Gram-negative bloodstream infections | [![PyPI](https://img.shields.io/pypi/v/respredai?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/respredai/) |
| [phenocluster](https://github.com/EttoreRocchi/phenocluster) | Unsupervised clinical phenotype discovery with survival and multistate modeling | [![PyPI](https://img.shields.io/pypi/v/phenocluster?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/phenocluster/) |
| [nestkit](https://github.com/EttoreRocchi/nestkit) | Nested cross-validation with calibration, threshold optimization, and statistical tests | [![PyPI](https://img.shields.io/pypi/v/nestkit?style=flat&logo=pypi&logoColor=white&label=&color=3775A9)](https://pypi.org/project/nestkit/) |

### Research Code

| Project | Description |
|---------|-------------|
| [CATS](https://github.com/Physics4MedicineLab/CATS) | Automated Cas9 nuclease comparison with ClinVar integration |
| [CAMISIM-BrokenStick](https://github.com/Physics4MedicineLab/CAMISIM-BrokenStick) | Broken stick model extension for metagenomic simulation |
| [APOBECSeeker](https://github.com/Physics4MedicineLab/APOBECSeeker) | APOBEC-style mutation identification from multiple sequence alignment |

### Latest Releases

<!-- LATEST-RELEASES:START -->
- [**MaldiSuite** v0.3.0](https://github.com/EttoreRocchi/MaldiSuite/releases/tag/v0.3.0) - 2026-10-30
- [**MaldiAMRKit** v0.22.1](https://github.com/EttoreRocchi/MaldiAMRKit/releases/tag/v0.22.1) - 2026-10-26
- [**MaldiAMRKit** v0.22.0](https://github.com/EttoreRocchi/MaldiAMRKit/releases/tag/v0.22.0) - 2026-10-22
- [**MaldiAMRKit** v0.21.0](https://github.com/EttoreRocchi/MaldiAMRKit/releases/tag/v0.21.0) - 2026-10-19
- [**ResPredAI** v1.9.4](https://github.com/EttoreRocchi/ResPredAI/releases/tag/v1.9.4) - 2026-09-30
<!-- LATEST-RELEASES:END -->

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
