import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/Home.vue'

import Departamento from '../views/Departamento.vue'
import Disciplina from '../views/Disciplina.vue'
import Cadastro from '../views/Cadastro.vue'
import Login from '../views/Login.vue'
import AreaAluno from '../views/AreaAluno.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cadastro',
    name: 'Cadastro',
    component: Cadastro
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/area_aluno',
    name: 'AreaAluno',
    component: AreaAluno
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/dpto/:departamento_slug',
    name: 'Departamento',
    component: Departamento
  },
  {
    path: '/dpto/:departamento_slug/:disciplina_slug',
    name: 'Disciplina',
    component: Disciplina
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
