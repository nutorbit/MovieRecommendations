<template>
    <el-container>
        <card v-for='(item, i) in getSimilar' :key='i' :obj='item'/>
    </el-container>
</template>

<script>
import card from '@/components/card'
import { mapGetters } from 'vuex';

export default {
    components: {
        card
    },
    computed: {
        ...mapGetters(['getSimilar'])
    },
}
</script>