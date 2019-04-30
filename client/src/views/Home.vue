<template>
  <div class='centered'>
    <div style='padding: 20vh;' class='box'>
      <h1>Movie Recommendation</h1>
      <el-autocomplete 
        v-model='search'
        :fetch-suggestions="querySearch"
        placeholder="Input name"
        :trigger-on-focus="false"
        value-key='title'
        @select="handleSelect"
      >
    
      </el-autocomplete>
    </div>
  </div>
</template>

<script>

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'home',
  data: () => {
    return {
      search: ''
    }
  },
  computed: {
    ...mapGetters(['getNames'])
  },
  methods: {
    ...mapActions(['loadNames', 'loadRecommend']),
    createFilter(queryString) {
      return (link) => {
        return (link.title.toLowerCase().includes(queryString.toLowerCase()) == true);
      };
    },
    querySearch(queryString, cb) {
      let links = this.getNames;
      let results = queryString ? links.filter(this.createFilter(queryString)) : links;
      cb(results);
    },
    handleSelect(item){
      this.loadRecommend(item.idx)
    }
  },
  mounted() {
    this.loadNames()
  }
}
</script>

<style>
.centered {
  position: fixed;
  top: 50%;
  left: 50%;
  /* bring your own prefixes */
  transform: translate(-50%, -50%);
}
.box {
  /* padding: 20vh;  */
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); 
  border-radius: 30px;
}
</style>

