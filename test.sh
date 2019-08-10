#1 init
python main.py init testClient testProject

if [[ -d "testClient" ]] && [[ -d "testClient/testProject" ]]; then
  echo "Init test passed"
fi

#1 add

cd testClient/testProject
python ../../main.py add --title testTask

if [[ -d "testTask" ]] && [[ -f "testTask/testTask.md" ]]; then
  echo "Add test passed"
fi

cd ../../

  rm -r testClient