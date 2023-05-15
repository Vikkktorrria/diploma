import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import "./maket/css/style.css"
import { createApp } from 'vue'
import App from './App.vue'
import components from '@/components/UI'
import router from "@/router/router";
import store from "@/store";

const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app
    .use(router)
    .use(store)
    .mount('#app')