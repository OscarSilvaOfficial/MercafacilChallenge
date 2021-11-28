<template>
  <div class="list">
    <h2 class='logo font-rem d-flex justify-center align-center' style='color: red; font-size: 6rem'>R&MFlix</h2>
    <vueper-slides
      v-if="showEpisedes"
      slide-multiple
      class="no-shadow mt-11"
      :visible-slides="6"
      :bullets="false"
      :arrows="false"
      :slide-ratio="1 / 6"
      :gap="5"
      :dragging-distance="70">
      <vueper-slide 
        :id="'character-' + character.name"
        :style="getBackground(character.image)" 
        class="bg-screen" 
        v-for="(character, i) in characters" 
        :key="i"
      />
    </vueper-slides>
  </div>
</template>

<script lang='ts'>
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore: Unreachable code error
import { VueperSlides, VueperSlide } from 'vueperslides'
import { Component, Vue } from 'vue-property-decorator';
import { GraphQLService } from '@/services/graphql'
import { ICharacter } from '@/intefaces/characters'
import { CHARACTERS } from './queries'
import 'vueperslides/dist/vueperslides.css'

@Component({
  components: { VueperSlides, VueperSlide },
})
export default class Characters extends Vue {

  graphql = new GraphQLService()
  characters?: ICharacter[]
  showEpisedes = false

  async created(): Promise<void> {
    const response: any = await this.graphql.get(CHARACTERS)
    this.characters = await response.data.data.characters.results
    this.showEpisedes = true
  }

  getBackground(image: string): string {
    return `background-image: url(${image}); background-size: cover`
  }
}
</script>

<style lang="scss">
.logo {
  margin-top: 2vh;
}
.bg-screen {
  transition: all .5s;
  opacity: .3;
  &:hover {
    transform: scale(1.1);
    opacity: 1;
    width: 200px;
  }
}
</style> 
