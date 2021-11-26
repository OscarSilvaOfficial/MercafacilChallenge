import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Episodes from '@/views/episodes/Episodes.vue'
import Characters from '@/views/characters/Characters.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/episodes',
    name: 'episodes',
    component: Episodes
  },
  {
    path: '/characters',
    name: 'characters',
    component: Characters
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
