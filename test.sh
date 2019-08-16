#1 init
python main.py init testClient testProject

PROJECT_PATH="testClient/testProject"

if [[ -d "testClient" ]] && [[ -d $PROJECT_PATH ]] &&
  [[ -d "$PROJECT_PATH/Backlog" ]] &&
  [[ -d "$PROJECT_PATH/Progress" ]] &&
  [[ -d "$PROJECT_PATH/Done" ]]; then
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