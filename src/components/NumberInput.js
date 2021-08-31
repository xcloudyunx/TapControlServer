import React from 'react';

import colors from "../config/colors";

export default function NumberInput(props) {
	return (
		<div style={styles.container}>
			<label style={styles.label}>
				{props.title}:
			</label>
			<button style={styles.button}>
				-
			</button>
			<input
				className={props.title.toLowerCase()}
				type="number"
				style={styles.input}
				value={props.value}
				onChange={props.onChange}
				min={1}
				max={props.max}
				disabled
			/>
			<button style={styles.button}>
				+
			</button>
		</div>
	);
}

const styles = {
	button: {
		backgroundColor: colors.transparent,
		color: colors.white,
		fontWeight: "bold",
		height: "100%",
		border: "1px solid "+colors.white,
	},
	container: {
		flex: 1,
		display: "flex",
		alignItems: "center",
	},
	input: {
		// flex: 2,
		backgroundColor: colors.transparent,
		color: colors.white,
		height: "100%",
		boxSizing: "border-box",
		border: "1px solid "+colors.white,
		textAlign: "center",
		fontSize: "5vh",
	},
	label: {
		flex: 1,
		color: colors.white,
		fontSize: "5vh",
	},
};