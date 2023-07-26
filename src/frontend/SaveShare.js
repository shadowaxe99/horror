import React, { useState } from 'react';
import { Button, Modal, Share } from 'react-native';

const SaveShare = ({ generatedStory, savedStories, setSavedStories }) => {
  const [modalVisible, setModalVisible] = useState(false);

  const saveStory = () => {
    setSavedStories([...savedStories, generatedStory]);
    setModalVisible(true);
  };

  const shareStory = async () => {
    try {
      const result = await Share.share({
        message: generatedStory,
      });

      if (result.action === Share.sharedAction) {
        if (result.activityType) {
          console.log('Shared with activity type of', result.activityType);
        } else {
          console.log('Shared');
        }
      } else if (result.action === Share.dismissedAction) {
        console.log('Share dismissed');
      }
    } catch (error) {
      console.error(error.message);
    }
  };

  return (
    <>
      <Button title="Save Story" onPress={saveStory} id="saveStoryButton" />
      <Button title="Share Story" onPress={shareStory} id="shareStoryButton" />

      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => {
          setModalVisible(!modalVisible);
        }}
      >
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <View style={{ backgroundColor: 'white', padding: 20, borderRadius: 10 }}>
            <Text>Story saved successfully!</Text>
            <Button
              title="Close"
              onPress={() => setModalVisible(!modalVisible)}
            />
          </View>
        </View>
      </Modal>
    </>
  );
};

export default SaveShare;