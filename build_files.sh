echo "BUILD START"
python3.9 -m pip install -r requirenments.txt
python3.9 manage.oy collectstatic --noinput --clear
echo "build end"