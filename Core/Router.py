"""
# !/usr/bin/env python
# File       : Router.py
# Time       ：2022/8/9 22:23
# Author     ：YuYe
"""
from fastapi import APIRouter
from Api.BaseRouter import ServiceRouter


AllRouter = APIRouter()


# API路由
AllRouter.include_router(ServiceRouter)