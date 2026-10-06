# Data Science Thesis Exploration & Research Handoff

## 📌 Project Overview
This document contains the curated research directions, domain-specific thesis titles, and core methodology tracks for a Data Science Master's/Ph.D. thesis utilizing **satellite remote sensing and earth observation data**. It serves as an official handoff prompt for downstream autonomous agents, research assistants, or academic advisors to begin literature reviews, data pipeline prototyping, or dataset sourcing.

---

## 🏛️ Domain Tracks & Curated Thesis Titles

### Track 1: Meteorology & Atmospheric Science
*Focus: Predicting extreme weather events, atmospheric dynamics, and resolution enhancement.*

1. **"Physics-Informed Deep Learning for Convective Storm Initiation Forecasting Using Geostationary Satellite Imagery"**
   * **Core Methodology:** Physics-Informed Neural Networks (PINNs), ConvLSTMs, Optical Flow.
   * **Primary Datasets:** GOES-R Series, Himawari-8/9, Meteosat Second Generation.
2. **"Spatiotemporal Graph Neural Networks for Tracking Atmospheric Dust and Aerosol Dispersion Metrics"**
   * **Core Methodology:** Spatiotemporal Graph Convolutional Networks (ST-GCN), Message Passing Neural Networks.
   * **Primary Datasets:** MODIS Atmosphere Products, Sentinel-5P (TROPOMI).
3. **"Super-Resolution Downscaling of Satellite-Derived Precipitation Data Using Generative Adversarial Networks (GANs)"**
   * **Core Methodology:** SRGAN, ESRGAN, Diffusion Models for Spatial Downscaling.
   * **Primary Datasets:** TRMM, GPM (Global Precipitation Measurement), IMERG.

### Track 2: Urban Development & Smart Cities
*Focus: Structural expansion, economic indicator tracking, and municipal resource planning.*

1. **"Predicting Informal Settlement Growth Patterns Using Deep Segment-Anything Models on Multi-Temporal Satellite Imagery"**
   * **Core Methodology:** Segment Anything Model (SAM) fine-tuning, Multi-temporal change detection, U-Net++.
   * **Primary Datasets:** Maxar Open Data, PlanetScope, Sentinel-2 (10m resolution).
2. **"Fusing Nighttime Light Satellite Radiometer Data with Mobility Metrics to Quantify Post-Disaster Economic Recovery"**
   * **Core Methodology:** Multimodal Data Fusion, Non-linear Time-Series Regression, Spatial Econometrics.
   * **Primary Datasets:** VIIRS Day/Night Band (DNB), Anonymized Mobility Data (SafeGraph/Google), LandScan.
3. **"An Object-Detection Approach to Quantifying Urban Green-Space Accessibility and Thermal Comfort Using Sentinel-2 Data"**
   * **Core Methodology:** YOLOv8/v10, Semantic Segmentation, Land Surface Temperature (LST) derivation.
   * **Primary Datasets:** Sentinel-2, Landsat 8/9 TIRS (Thermal Infrared Sensor).

### Track 3: Astronomy & Earth-Observation Synergy
*Focus: Cross-domain transfer learning, light pollution mapping, and planetary topology analogs.*

1. **"Quantifying Light Pollution Dynamics and Ecological Disruption Using Multi-Spectral Nighttime Satellite Imagery"**
   * **Core Methodology:** Automated Radiometric Calibration, Random Forest/Gradient Boosting, Spatial Clustering.
   * **Primary Datasets:** VIIRS DNB, JL1-3B (High-resolution night lights), ISS Nighttime Photography.
2. **"Cross-Domain Deep Learning: Adapting Astronomical Source-Detection Algorithms for Terrestrial Satellite Feature Extraction"**
   * **Core Methodology:** Transfer Learning, Source Extractor (SExtractor) adaptations, Self-Supervised Vision Transformers.
   * **Primary Datasets:** Hubble Space Telescope / JWST pipelines (source domains), WorldView/PlanetScope (target domains).
3. **"Unsupervised Contrastive Learning for Classifying Martian and Terrestrial Surface Features: A Satellite Topology Study"**
   * **Core Methodology:** SimCLR / MoCo v3 Contrastive Learning, Topological Data Analysis (TDA), Autoencoders.
   * **Primary Datasets:** USGS Earth Resources Observation (EROS), Mars Reconnaissance Orbiter (MRO) HiRISE / CTX.

---

## 🛠️ Technical Competency Checklist & Constraints
When prompting an engineering agent to initialize this repository, ensure the following architecture requirements are passed:
* **Storage & Scale:** Cloud-optimized formats like **Cloud-Optimized GeoTIFFs (COGs)** and spatial **Parquet/GeoParquet** tables.
* **Compute Environments:** Heavy integration with **Google Earth Engine (GEE) Python API**, AWS Open Data Registry, or Microsoft Planetary Computer.
* **Core Packages:** `rasterio`, `geopandas`, `rioxarray`, `xarray`, `shapely`, `torchgeo` (PyTorch for Earth Observation), and `segment-earth`.

---

## 🤖 Next-Action Agent Prompt
*Copy and paste the string below directly into your AI coding assistant or research agent to begin execution:*

```text
You are an expert remote sensing data scientist and academic research assistant. I am handing off a master's thesis framework to you. Your task is to select the most viable thesis title from the provided list based on data openness, write a comprehensive 3-page literature review outline, draft a data collection python pipeline using Google Earth Engine / Planetary Computer API, and establish a baseline PyTorch/Scikit-Learn modeling architecture workflow. 

Review the provided tracks: 
1. Meteorology (Storms, Aerosols, Downscaling GANs)
2. Urban Development (SAM Segmentations, Nightlights Fusion, Green-Space LST)
3. Astronomy Synergy (Light Pollution, Cosmic Source-Detection to Earth, Martian Topography)

Acknowledge receipt of this handoff. Recommend the top 2 titles that have the lowest barrier to entry regarding free, open-access cloud data, and provide the initial directory structure for a GitHub repository designed to handle this data scale.
```
