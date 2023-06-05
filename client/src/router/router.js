import { createRouter, createWebHistory } from "vue-router";
import UserProfile from "@/pages/UserProfile";
import LogIn from "@/pages/LogIn";
import StudentPage from "@/pages/StudentPage";
import StudentRegistration from "@/pages/StudentRegistration";
import DisciplinesPage from "@/pages/DisciplinePage";
import TrajectoryPage from "@/pages/TrajectoryPage";
import TempPage from "@/pages/TempPage";
import SettingsPage from "@/pages/SettingsPage";
import CompetencePage from "@/pages/CompetencePage";

const routes = [
    {
        path: '/',
        component: LogIn
    },
    {
        path: '/profile',
        name: 'profile',
        component: UserProfile
    },
    {
        path: '/login',
        name: 'login',
        component: LogIn
    },
    {
        path: '/student/all',
        name: 'studentPage',
        component: StudentPage
    },
    {
        path: '/student/registration',
        name: 'studentRegistration',
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
    {
        path: '/test',
        component: TempPage
    },
    {
        path: '/settings',
        component: SettingsPage
    },
    {
        path: '/competence',
        component: CompetencePage
    },
]

const router = createRouter( {
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router