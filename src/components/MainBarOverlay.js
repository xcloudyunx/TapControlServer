import React from 'react';

import constants from "../config/constants";

import TextElement from "../components/TextElement";
import Button from "../components/Button";

export default function MainBarOverlay(props) {
	return (
		<div style={styles.container}>
			<Button
				value="&lArr;"
				onClick={() => {props.onClick(props.currentPage-1)}}
			/>
			<TextElement
				value={props.currentPage}
				style={styles.text}
			/>
			<Button
				value="&rArr;"
				onClick={() => {props.onClick(props.currentPage+1)}}
			/>
		</div>
	);
};

const styles = {
	container: {
		width: "100%",
		height: "100%",
		position: "absolute",
		display: "flex",
		justifyContent: "space-between",
		alignItems: "center",
	},
	text: {
		paddingBottom: "3%",
		alignSelf: "flex-end",
	}
};