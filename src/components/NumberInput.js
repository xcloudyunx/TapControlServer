import React from 'react';

import colors from "../config/colors";

import TextElement from "./TextElement";
import Button from "./Button";

export default function NumberInput(props) {
	return (
		<div style={styles.container}>
			<label style={styles.label}>
				{props.title}:
			</label>
			<div style={styles.adjuster}>
				<Button
					value="-"
					onClick={() => {props.onClick(props.value-1)}}
					style={styles.button}
				/>
				<TextElement
					value={props.value}
					style={styles.text}
					disabled
				/>
				<Button
					value="+"
					onClick={() => {props.onClick(props.value+1)}}
					style={styles.button}
				/>
			</div>
		</div>
	);
}

const styles = {
	adjuster: {
		flex: 1,
		display: "flex",
	},
	button: {
		flex: 1,
	},
	container: {
		flex: 1,
		display: "flex",
		alignItems: "center",
	},
	label: {
		flex: 2,
		color: colors.white,
	},
	text: {
		flex: 2,
	}
};