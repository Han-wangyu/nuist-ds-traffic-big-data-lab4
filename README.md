# 交通流量模拟与可视化系统

## 项目概述
本项目旨在模拟真实交通场景中的车辆运行情况，对车辆运行数据进行仿真并可视化展示。系统包含基础交通流量模拟和进阶特殊场景模拟两个主要部分。

## 功能特性

### 基础功能
- 地图节点(路口)和边(道路)的定义与管理
- 基于时序的车辆生成系统
- 使用Dijkstra算法的路径规划
- 车辆位置实时更新
- 基础可视化展示

### 进阶功能
- 非等概率车辆出入口模拟
- 时变车流量模拟
- 交通信号灯系统
- 车辆拥堵情况模拟

## 核心任务

### 任务1：车辆位置可视化
- 在任意采样时间点展示所有车辆位置
- 支持地图背景显示
- 车辆位置实时更新

### 任务2：道路拥堵可视化
- 类似导航软件的道路拥堵展示
- 使用红绿线标识拥堵程度
- 实时更新拥堵状态

### 任务3：拥堵情况统计
- 特定道路拥堵情况时序图
- 支持历史数据查询
- 拥堵趋势分析

### 任务4：实时路径规划
- 基于当前路况的最短时间路径规划
- 动态更新路径建议
- 多路径方案对比

## 数据结构

### 车辆对象
- 位置信息
- 速度信息
- 方向信息
- 可扩展属性

### 路径对象
- 路口索引序列
- 长度可变
- 支持动态更新

### 路口对象
- 位置信息
- 相连道路信息
- 交通信号灯状态
- 可扩展属性

## 项目结构 

```
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── vehicle.py
│   │   ├── road.py
│   │   ├── intersection.py
│   │   └── traffic_light.py
│   ├── simulation/
│   │   ├── __init__.py
│   │   ├── simulator.py
│   │   ├── path_planning.py
│   │   └── traffic_flow.py
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── gui.py
│   │   └── plotting.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── data/
│   ├── maps/
│   │   ├── simple_map.jpg
│   │   └── complex_map.png
│   └── config/
│       └── simulation_params.json
└── tests/
    ├── __init__.py
    └── test_simulation.py
```


## 技术栈
- Python 3.8+
- NumPy: 数值计算
- Matplotlib: 数据可视化
- PyQt5: GUI界面
- NetworkX: 图论算法

## 运行环境
- Python 3.8或更高版本
- 相关依赖包(见requirements.txt)