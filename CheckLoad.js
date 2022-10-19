(function() {//causes this function to run immediately

  Scene_OmoriFile.prototype.loadGame = function() {
      if (DataManager.loadGame(this.savefileId())) {

        $gameParty.changeWorldItemContainer(1);

        SoundManager.playLoad();
        this.fadeOutAll();
        // Reload Map if Updated
        if ($gameSystem.versionId() !== $dataSystem.versionId) {
          $gamePlayer.reserveTransfer($gameMap.mapId(), $gamePlayer.x, $gamePlayer.y);
          $gamePlayer.requestMapReload();
        };
        SceneManager.goto(Scene_Map);
        var info = DataManager.loadSavefileInfo(this.savefileId());
        $gameSystem.saveName = info.saveName;
        this._loadSuccess = true;
        // Close Prompt Window
        this._promptWindow.close();
        this._promptWindow.deactivate();
      } else {
        // Play Buzzer
        SoundManager.playBuzzer();
        // Close Prompt Window
        this._promptWindow.close();
        this._promptWindow.deactivate();
        // Set Can select Flag to true
        this._canSelect = true;
      };
    };

})();//causes this function to run immediately