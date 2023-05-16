import { createRouter, createWebHistory } from "vue-router";
import UserProfile from "@/pages/UserProfile";
import LogIn from "@/pages/LogIn";
import StudentPage from "@/pages/StudentPage";
import StudentRegistration from "@/pages/StudentRegistration";
import DisciplinesPage from "@/pages/DisciplinesPage";
import Main from "@/pages/MainPage";
import TrajectoryPage from "@/pages/TrajectoryPage";

const routes = [
    {
        path: '/',
        component: Main
    },
    {
        path: '/profile',
        component: UserProfile
    },
    {
        path: '/login',
        name: 'login',
        component: LogIn
    },
    {
        path: '/student/all',
        component: StudentPage
    },
    {
        path: '/student/registration',
        component: StudentRegistration
    },
    {
        path: '/disciplines',
        name: 'disciplines',
        component: DisciplinesPage
    },
    {
        path: '/trajectory',
        name: 'trajectory',
        component: TrajectoryPage
    },
]

const router = createRouter( {
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router