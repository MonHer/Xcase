"""
# !/usr/bin/env python
# File       : FileModule.py
# Time       ：2022/8/9 23:24
# Author     ：YuYe
"""
from typing import List
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import HTMLResponse

app = APIRouter()


@app.post("/files/", name='上传文件接口')
async def create_files(files: List[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/upload/files/", name='上传文件接口')
async def create_upload_files(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}
