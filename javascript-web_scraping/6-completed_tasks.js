#!/usr/bin/node
const request = require('request');

const apiURL = 'https://jsonplaceholder.typicode.com/todos';

async function computeCompletedTasks(apiURL) {
  try {
    const response = await axios.get(apiURL);
    const todos = response.data;

    const userCompletedTasks = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        const userId = todo.userId;
        userCompletedTasks[userId] = (userCompletedTasks[userId] || 0) + 1;
      }
    });

    return userCompletedTasks;
  } catch (error) {
    console.error(`Error fetching data: ${error.message}`);
    return null;
  }
}

async function main() {
  const completedTasks = await computeCompletedTasks(apiURL);

  if (completedTasks) {
    console.log('Number of completed tasks by user id:');
    for (const userId in completedTasks) {
      console.log(`User ID ${userId}: ${completedTasks[userId]} completed tasks`);
    }
  }
}

main();

