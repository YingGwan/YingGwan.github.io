---
title: "[**Conference Article**] Function Based Sim-to-Real Learning for Shape Control of Deformable Free-form Surfaces"
Authors: 'Y. Tian, G. Fang, R. Su, W. Wang, S. Gill, A. Weightman, and C.C.L. Wang'
collection: publications
permalink: /publication/RSS2024FuncSim2Real
excerpt: '**[1st Author]** Function based learning enables traning from sparse and incomplete dataset'
date: 2024-05-20
venue: 'Robotics Science and Systems Conference 2024, TU Delft'
---
For the shape control of deformable free-form surfaces, simulation plays a crucial role in establishing the mapping between the actuation parameters and the deformed shapes. 
The differentiation of this forward kinematic mapping is usually employed to solve the inverse kinematic problem for determining the actuation parameters that can realize a target shape. 
However, the free-form surfaces obtained from simulators are always different from the physically deformed shapes due to the errors introduced by hardware and the simplification adopted in physical simulation. 
To fill the gap, we propose a novel deformation function based sim-to-real learning method that can map the geometric shape of a simulated model into its corresponding shape of the physical model. 
Unlike the existing sim-to-real learning methods that rely on completely acquired dense markers, our method accommodates sparsely distributed markers and can resiliently use all captured frames -- even for those in the presence of missing markers. 
To demonstrate its effectiveness, our sim-to-real method has been integrated into a neural network-based computational pipeline designed to tackle the inverse kinematic problem on a pneumatically actuated deformable mannequin.

[Download arxiv Version](https://arxiv.org/abs/2405.08935)
[Video@YouTube](https://www.youtube.com/watch?v=iBmc2u_2-rI&t=2s)