import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import axios from 'axios';

import App from './App.vue';
import router from './router';
import store from './store'; // New

const app = createApp(App);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://10.10.132.214:5000/';  // the FastAPI backend

app.use(router);
app.use(store); // New
app.mount("#app");
