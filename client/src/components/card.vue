<template>
    <el-col :span="4">
        <el-card :body-style="{ padding: '0px' }" shadow="hover">
        <img v-bind:src="obj.poster" class="image" width='300px' height="300px">
        <div style="padding: 14px;">
            <span>{{obj.title}}</span>
            <div class="bottom clearfix">
            <el-link v-bind:href='obj.link'>Link</el-link>
            </div>
        </div>
        </el-card>
    </el-col>
</template>

<script>
export default {
    props: ['obj']
}
</script>
