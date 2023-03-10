import Profile from "@/pages/Profile";
import { createRouter } from "vue-router";

const routes = [
    {
        path: '/',
        component: Profile
    }
]

const router = createRouter( {
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router