#!/bin/sh

timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
echo "=== Updating SSF Repo: log entry $timestamp ==="
cd ~/Student-Startup-Festival;
git pull;
echo "==========================="

