import Vue from 'vue'
import Vuex from 'vuex'
import { URL } from '@/constants/index.js'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movie_name: null,
    similar: null
  },
  mutations: {
    loadNames(state){
      axios.get(URL+'/getNames').then((res) => {
        state.movie_name = res.data.list_name
      }).catch( (err) => {
        console.log(err)
      })
    },
    loadRecommend(state, _id){
      // console.log(_id)
      axios.post(URL+'/getSimilar', {id: _id} ).then( (res) => {
        state.similar = res.data.result
      })
    }
  },
  getters:{
    getNames(state){
      return state.movie_name
    },
    getSimilar(state){
      return state.similar
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
