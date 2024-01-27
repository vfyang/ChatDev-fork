'''
This is the main JavaScript file that initializes the Vue.js application.
'''
new Vue({
  el: '#app',
  data: {
    tasks: [],
    users: [],
    newTask: {
      title: '',
      description: '',
      priority_level: '',
      assignment: '',
      ending_date: ''
    },
    newUser: {
      username: '',
      email: ''
    }
  },
  methods: {
    addTask: function() {
      // Submit form data to the server
      axios.post('/tasks', this.newTask)
        .then(response => {
          this.tasks.push(response.data);
          this.newTask = {
            title: '',
            description: '',
            priority_level: '',
            assignment: '',
            ending_date: ''
          };
        });
    },
    addUser: function() {
      // Submit form data to the server
      axios.post('/users', this.newUser)
        .then(response => {
          this.users.push(response.data);
          this.newUser = {
            username: '',
            email: ''
          };
        });
    }
  },
  created: function() {
    // Fetch tasks and users from the server
    axios.get('/tasks')
      .then(response => {
        this.tasks = response.data;
      });
    axios.get('/users')
      .then(response => {
        this.users = response.data;
      });
  }
});