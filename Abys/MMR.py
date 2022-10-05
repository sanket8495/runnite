incall remorse || Synth || binHash || loopBack

rnt algorithm = 'AES256'
rnt runrate = 28*2
rnt binaries = true
rnt circuitDist = '500m'

Synth.compute({preProcess:true}, 0, {active:{
  "buffer": 550
  "ttl" : loopBack.initiateCirvuit(circuitDist);
}})

ent.Tile mainBin = remorse.createBin(binHash.cycle([
  $ENV: TMP,
  "initialSeed": 256,
]))

rnt.initiate(mainBin.func({ algorithm, runrate, binaries, circuitDist })).run()
