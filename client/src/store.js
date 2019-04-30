import Vue from 'vue'
import Vuex from 'vuex'
import { URL } from '@/constants/index.js'
import axios from 'axios'
import router from '@/router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movie_name: null,
    similar: null,
    main: null,
    random: null,
    popular: null
  },
  mutations: {
    loadNames(state){
      axios.get(URL+'/getNames').then((res) => {
        state.movie_name = res.data.list_name
      })

      axios.get(URL+'/getRandom').then( (res) => {
        state.random  = res.data.result
      })

      axios.get(URL+'/getPopular').then( (res) => {
        state.popular = res.data.result
      })

    },
    loadRecommend(state, _id){
      // console.log(_id)
      axios.post(URL+'/getSimilar', {id: _id} ).then( (res) => {
        state.main    = res.data.result[0]
        state.similar = res.data.result.slice(1, 6)
        router.push({'name': 'display'})
      })
    }
  },
  getters:{
    getNames(state){
      return state.movie_name
    },
    getSimilar(state){
      return state.similar
    },
    getMain(state){
      return state.main
    },
    getRandom(state){
      return state.random
    },
    getPopular(state){
      return state.popular
    }
  },
  actions: {
    loadNames(context){
      context.commit('loadNames')
    },
    loadRecommend(context, _id){
      context.commit('loadRecommend', _id)
    }
  }
})
