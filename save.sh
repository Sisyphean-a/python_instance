#!/bin/bash
echo "请输入你的commit："
read be
git add --all
git commit -m "$be"
git push
