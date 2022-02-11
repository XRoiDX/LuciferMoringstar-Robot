if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/XRoiDX/Black-Panther-.git /Black-Panther-
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Black-Panther-
fi
cd /LuciferMoringstar-Robot
pip3 install -U -r requirements.txt
echo "Starting LuciferMoringstar RoBot...."
python3 main.py
