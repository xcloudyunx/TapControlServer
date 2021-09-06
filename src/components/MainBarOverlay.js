import React from 'react';

import TextElement from "../components/TextElement";
import Button from "../components/Button";

export default function MainBarOverlay(props) {
	return (
		<div style={styles.container}>
			<Button
				value="&lArr;"
				onClick={() => {props.onClick(props.currentPage-1)}}
				style={styles.button}
			/>
			<TextElement
				value={props.currentPage}
				style={styles.text}
			/>
			<Button
				value="&rArr;"
				onClick={() => {props.onClick(props.currentPage+1)}}
				style={styles.button}
			/>
		</div>
	);
};

const styles = {
	button: {
		visibility: "visible",
	},
	container: {
		width: "100%",
		height: "100%",
		position: "absolute",
		display: "flex",
		justifyContent: "space-between",
		alignItems: "center",
		visibility: "hidden",
	},
	text: {
		paddingBottom: "3%",
		alignSelf: "flex-end",
		visibility: "visible",
	},
};