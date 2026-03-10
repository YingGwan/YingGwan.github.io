---
title: "[**Journal Article**] Model-Free Co-Optimization of Manufacturable Sensor Layouts and Deformation Proprioception"
Authors: 'Y. Tian, G. Fang, A. Lyu, X. Wang, Z. Shi, Y. Guo, W. Wang, and C.C.L. Wang'
collection: publications
permalink: /publication/TRO2026SensorOpt
excerpt: '**[1st Author]** Task-gradient optimization for sparse, physics-ready sensor layouts with manufacturability constraints'
date: 2026-03-01
venue: 'IEEE Transactions on Robotics'
---
Are massive, densely-packed sensor arrays truly better? Does designing them manually via trial-and-error have to be so painstakingly time-consuming? No! We present a novel simulator-free computational design framework that uses **task gradients** to optimize an initial massive number of random sensors down to a sparse, physics-ready, and highly accurate layout. By encoding strict discrete fabrication rules into **differentiable loss functions**, our method autonomously co-optimizes the sensor layout alongside a shape prediction network via end-to-end gradient descent.

<a href="https://youtu.be/dKYubu_igog" target="_blank">
  <img src="https://img.youtube.com/vi/dKYubu_igog/maxresdefault.jpg" alt="Watch the video" width="100%" />
</a>

Our framework concurrently optimizes both the continuous spatial placement and discrete number of flexible sensors alongside neural network parameters for 3D shape prediction. A core novelty of our approach is reformulating inherently discrete fabrication requirements into **differentiable loss functions** (Overlap-free, Inter-sensor distance, and Length preference).

[Paper PDF](https://github.com/YingGwan/SensorOpt/blob/main/TROSensorCoOptm_FinalVer.pdf) | [Code on GitHub](https://github.com/YingGwan/SensorOpt/tree/main) | [Video@YouTube](https://www.youtube.com/watch?v=dKYubu_igog)
