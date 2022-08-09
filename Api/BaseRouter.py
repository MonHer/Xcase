"""
# !/usr/bin/env python
# File       : BaseRouter.py
# Time       ：2022/8/9 22:23
# Author     ：YuYe
"""
from fastapi import APIRouter
from Crud.FileModule import app


ServiceRouter = APIRouter(prefix='/api', tags=['api路由'])

ServiceRouter.include_router(app)