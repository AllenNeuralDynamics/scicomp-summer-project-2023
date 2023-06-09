import h5py
with h5py.File('labels.v002.000_centered_pair_small.analysis.h5', 'r') as f:
    occupancy_matrix = f['track_occupancy'][:]
    tracks_matrix = f['tracks'][:]

print(occupancy_matrix.shape)
print(tracks_matrix.shape)
