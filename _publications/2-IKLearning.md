---
title: "[**Article**] Efficient Jacobian-Based Inverse Kinematics With Sim-to-Real Transfer of Soft Robots by Learning"
collection: publications
permalink: /publication/SoRoIKLearning
excerpt: '**[2nd Author]** Jacobian Learning Plus Sim2Real Transfer of Soft Robots'
date: 2022-06-03
venue: 'IEEE/ASME Transactions on Mechatronics'
paperurl: 'https://ieeexplore.ieee.org/document/9790339'
citation: 'G. Fang, Y. Tian, Z. -X. Yang, J. M. P. Geraedts and C. C. L. Wang, "Efficient Jacobian-Based Inverse Kinematics With Sim-to-Real Transfer of Soft Robots by Learning," in IEEE/ASME Transactions on Mechatronics, 2022'
---
This article presents an efficient learning-based method to solve the inverse kinematic (IK) problem on soft robots with highly nonlinear deformation. The major challenge of efficiently computing IK for such robots is due to the lack of analytical formulation for either forward or inverse kinematics. 
To address this challenge, we employ neural networks to learn both the mapping function of forward kinematics and also the Jacobian of this function. As a result, Jacobian-based iteration can be applied to solve the IK problem. A sim-to-real training transfer strategy is conducted to make this approach more practical. 
We first generate a large number of samples in a simulation environment for learning both the kinematic and the Jacobian networks of a soft robot design. Thereafter, a sim-to-real layer of differentiable neurons is employed to map the results of simulation to the physical hardware, 
where this sim-to-real layer can be learned from a very limited number of training samples generated on the hardware.

[Download arxiv Version](https://arxiv.org/pdf/2012.13965.pdf)
[Video@YouTube](https://www.youtube.com/watch?v=vv7u0SkDXCQ&feature=youtu.be)