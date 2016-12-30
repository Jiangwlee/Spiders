# Spiders

## About

This is a project to practice writing Scrapy based crawlers. Every project has a seperate directory and been tested by myself. Some projects relays on Scrapy-Splash which is a lightweight browser. It can render javascripts and get back a dynamic generated html. For these projects, users should have Splash and Scrapy-Splash installed in advance.

## Projects

* newsmthimages
    * This project implements a crawler named 'newsmth' which could download static (.jpg) and dynamic (.gif) images from http://newsmth.net.

# 中文说明

## 概述

这个项目是个人基于Scrapy写的一些用于练手的爬虫项目。每个项目均有一个独立的目录，并且经过本人的简单测试，可以正常运行。有些项目依赖于Scrapy-Splash。它类似于一个轻量的浏览器，可以渲染基于Javascript的动态网页，并把渲染的结果返回给Scrapy。对于这些项目，如果想正常的运行爬虫，需要首先安装Splash和Scrapy-Splash。我的开发环境是Ubuntu，并且基于Docker安装和运行着一个Splash容器，然后在Scrapy项目中启用了Scrapy-Splash中间件，从而能够正常的爬取动态网页。

## 项目说明

* newsmthimages
    * 实现了一个名为newsmth的爬虫，能够从水木清华的贴图版爬取第一页的所有帖子中的图片，包括静态图片和动态图片，并将图片按照目录保存。每个目录的名字为帖子的名字。
