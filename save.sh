#!/bin/bash
echo "请输入你的commit："
read commit
git add --all
git commit -m "$commit"
git push
