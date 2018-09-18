import { StyleSheet } from 'react-native';

export default StyleSheet.create({
  // sass --watch style.scss style.css
  'p': {
    'margin': [{ 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }]
  },
  'body': {
    'font': [{ 'unit': '%V', 'value': 1 }, { 'unit': 'string', 'value': 'Helvetica,' }, { 'unit': 'string', 'value': 'sans-serif' }],
    'color': '#333',
    'margin': [{ 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }],
    'border': [{ 'unit': 'px', 'value': 5 }, { 'unit': 'string', 'value': 'solid' }, { 'unit': 'string', 'value': '#eeeeee' }]
  }
});
