---
title: "[**Journal Article**] Correspondence-Free, Function-Based Sim-to-Real Learning for Deformable Surface Control"
Authors: 'Y. Tian, G. Fang, R. Su, A. Lyu, N. Dutta, W. Wang, S. Gill, A. Weightman, and C.C.L. Wang'
collection: publications
permalink: /publication/TRO2025CorreFreeSim2Real
excerpt: '**[1st Author]** Correspondence-free sim-to-real learning for general surface modelling and control'
date: 2025-12-01
venue: 'IEEE Transactions on Robotics'
---
Are you tired of sim-to-real transfer methods demanding perfect, dense marker correspondences? What if you could learn deformation functions directly from partial, noisy 3D scans or motion capture data with missing markers? We present a novel correspondence-free, function-based sim-to-real learning method for controlling deformable freeform surfaces. Unlike traditional approaches, our method simultaneously learns a deformation function space and a confidence map to bridge the sim-to-real gap, tolerating highly imperfect real-world observations!

<img src="https://yinggwan.github.io/CFS2R.github.io/static/images/Pipeline.png" alt="Pipeline" width="100%" />

Our approach simultaneously learns a deformation function space and a confidence map -- both parameterized by a neural network -- to map simulated shapes to their real-world counterparts. As a result, the sim-to-real learning can be conducted by input from either a 3D scanner as point clouds (without correspondences) or a motion capture system as marker points (tolerating missed markers). The resultant sim-to-real transfer can be seamlessly integrated into a neural network-based computational pipeline for inverse kinematics and shape control.

We demonstrate the versatility and adaptability of our method on two vision devices and across four pneumatically actuated soft robots: a deformable membrane, a robotic mannequin, and two soft manipulators.

[Paper PDF](https://arxiv.org/abs/2509.00060) | [Code on GitHub](https://github.com/YingGwan/FunctionBasedSim2RealLearning) | [Project Page](https://yinggwan.github.io/CFS2R.github.io/)
