<template>
    <div>
        <h1>Result</h1>
        <el-row type='flex' justify="center">
            <card :obj='getMain'/>
        </el-row>
        <br>
        <div style="padding: 2vh;" class='box'>
            <h1>Similar context</h1>
            <el-row type='flex' justify="space-around">
                <card v-for='(item, i) in getSimilar' :key='i' :obj='item'/>
            </el-row>
        </div>
        <br>
        <div style="padding: 2vh;" class='box'>
            <h1>Popular</h1>
            <el-row type='flex' justify="space-around">
                <card v-for='(item, i) in getPopular' :key='i' :obj='item'/>
            </el-row>
        </div>
        <br>
        <div style="padding: 2vh;" class='box'>
            <h1>Random</h1>
            <el-row type='flex' justify="space-around">
                <card v-for='(item, i) in getRandom' :key='i' :obj='item'/>
            </el-row>
        </div>
    </div>
</template>

<script>
import card from '@/components/card'
import { mapGetters } from 'vuex';

export default {
    components: {
        card
    },
    computed: {
        ...mapGetters(['getSimilar', 'getMain', 'getRandom', 'getPopular'])
    },
}
</script>