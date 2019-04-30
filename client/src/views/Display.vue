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
            <el-carousel :interval="2500" type="card" height="40vh">
                <el-carousel-item v-for="(item, i) in getRandom" :key="i">
                        <img v-bind:src="item.poster" class="image" width='300px' height="300px">
                        <div style="padding: 14px;">
                            <span>{{item.title}}</span>
                            <div class="bottom clearfix">
                            <el-link v-bind:href='item.link'>Link</el-link>
                            </div>
                        </div>
                </el-carousel-item>
            </el-carousel>
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