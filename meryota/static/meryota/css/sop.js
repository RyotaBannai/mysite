import { StyleSheet } from 'react-native';

export default StyleSheet.create({
  'paragraph::before': {
    'content': ''\2003\2003''
  },
  'body': {
    'margin': [{ 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }]
  },
  'container': {
    'color': '#212121',
    'fontSize': [{ 'unit': 'em', 'value': 1.6 }],
    'lineHeight': [{ 'unit': 'em', 'value': 1.4 }],
    'border': [{ 'unit': 'px', 'value': 5 }, { 'unit': 'string', 'value': 'solid' }, { 'unit': 'string', 'value': '#eee' }],
    'padding': [{ 'unit': 'px', 'value': 30 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }, { 'unit': 'px', 'value': 0 }]
  },
  'container > div:nth-child(1) > p': {
    'color': '#333',
    'fontSize': [{ 'unit': 'em', 'value': 1.5 }],
    'textAlign': 'center'
  },
  'container > div:nth-child(2) > p': {
    'marginBottom': [{ 'unit': 'px', 'value': 10 }],
    'color': '#333',
    'fontSize': [{ 'unit': 'em', 'value': 1.1 }],
    'textAlign': 'center'
  },
  'container > divdep > p': {
    'marginTop': [{ 'unit': 'px', 'value': 0 }],
    'color': '#333',
    'fontSize': [{ 'unit': 'em', 'value': 1.1 }],
    'textAlign': 'center'
  },
  'container > div#statement': {
    'padding': [{ 'unit': 'px', 'value': 30 }, { 'unit': 'px', 'value': 90 }, { 'unit': 'px', 'value': 75 }, { 'unit': 'px', 'value': 90 }]
  },
  'footer': {
    'width': [{ 'unit': '%H', 'value': 1 }],
    'height': [{ 'unit': 'px', 'value': 100 }],
    'bottom': [{ 'unit': 'px', 'value': 0 }],
    'overflow': 'hidden'
  }
});
