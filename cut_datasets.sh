#!/bin/sh

k=1
n=450
for i in $(cat pdb_list.txt);do
	k=`expr $k + 1`
	if [ $k -gt 450 ];then
		cp ./flags/${i}.png ~/huangh/fcn_learnig/FCN-TensorFlow/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/annotations/validation
		cp ./image_rgb/${i}.jpg ~/huangh/fcn_learnig/FCN-TensorFlow/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/images/validation
		echo $i >>validation_list.txt
	else
		cp ./flags/${i}.png ~/huangh/fcn_learnig/FCN-TensorFlow/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/annotations/training
                cp ./image_rgb/${i}.jpg ~/huangh/fcn_learnig/FCN-TensorFlow/Data_zoo/MIT_SceneParsing/ADEChallengeData2016/images/training
                echo $i >>training_list.txt
	fi
done
