<template>
  <div class="list">
    <vueper-slides
      class="no-shadow mt-4"
      :visible-slides="6"
      :arrows="false"
      :slide-ratio="1 / 4"
      :gap="3"
      :dragging-distance="70">
      <vueper-slide class="bg-screen" v-for="i in 9" :key="i" :title="i.toString()" />
    </vueper-slides> 
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore: Unreachable code error
import { VueperSlides, VueperSlide } from 'vueperslides'

@Component({
  components: { VueperSlides, VueperSlide },
})
export default class Episodes extends Vue {}
</script>

<style lang="scss" scoped>
.bg-screen {
  background-image: url('../../assets/img/menu-icon.jpg');
  transition: all .5s;
  opacity: .3;
  &:hover {
    transform: scale(1.1);
    opacity: 1;
  }
}

</style> 