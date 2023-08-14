import React from "react";
import { View, Button, TextInput, StyleSheet } from "react-native";

export default function App() {
  return (
    <View style={styles.screen}>
      <View style={styles.inputContainer}>
        <TextInput placeholder="목표 입력" style={styles.input} />
        <Button title="추가" />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    padding: 30,
  },
  inputContainer: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  input: {
    flexBasis: "80%",
    borderColor: "black",
    borderWidth: 1,
    padding: 10,
  },
});